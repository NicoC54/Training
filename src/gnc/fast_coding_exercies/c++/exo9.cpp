/* ============================================================================
 * EXERCICE 3 : Gestionnaire de commande d'actionneurs (Strategy Pattern)
 * ============================================================================
 *
 * CONTEXTE :
 * Dans un système de guidage et contrôle (GNC), la boucle de commande calcule
 * les consignes d'actionnement (forces, couples, poussées) à partir de l'état
 * estimé et de la cible visée.
 * Pour tester différentes lois de commande sans modifier la logique d'exécution
 * (open/closed principle), on isole l'algorithme derrière une interface et on
 * l'injecte dans le pipeline d'actionnement.
 *
 * CAHIER DES CHARGES :
 *
 * 1. Structures de données :
 *    - using Vector3d = std::array<double, 3>;
 *    - struct State {
 *          Vector3d position{0.0, 0.0, 0.0};
 *          Vector3d velocity{0.0, 0.0, 0.0};
 *      };
 *
 * 2. Interface 'IController' (Stratégie abstraite) :
 *    - Destructeur virtuel obligatoire.
 *    - virtual Vector3d compute_control(const State& current,
 *                                       const State& target,
 *                                       double dt) = 0;
 *
 * 3. Stratégie concrète 1 : 'PidController' :
 *    - Constructeur prenant les gains : Kp, Ki, Kd (double).
 *    - Implémente le calcul proportionnel/dérivé/intégral sur l'erreur de position
 *      (pour simplifier, tu peux appliquer le calcul composante par composante).
 *    - Conserve l'intégrale de l'erreur dans un état interne.
 *
 * 4. Stratégie concrète 2 : 'BangBangController' :
 *    - Constructeur prenant une valeur de commande maximale : max_output (double).
 *    - Renvoie +max_output si target > current, -max_output sinon (par axe).
 *
 * 5. Contexte d'exécution : 'ActuatorPipeline' :
 *    - Reçoit l'algorithme de contrôle à la construction par INJECTION DE DÉPENDANCE
 *      via un std::unique_ptr<IController>.
 *    - Méthode 'step(const State& current, const State& target, double dt)' :
 *        Délègue le calcul au contrôleur actif et renvoie la commande.
 *    - Méthode 'set_controller(std::unique_ptr<IController> new_controller)' :
 *        Permet de permuter de loi de commande à chaud pendant le vol.
 *
 * CONTRAINTES :
 * - Zéro dépendance externe (std::array standard pour Vector3d, pas d'Eigen requis ici).
 * - Transfert propre de propriété (std::unique_ptr et std::move).
 * - Const-correctness stricte.
 * ============================================================================
 */

#pragma once

#include <array>
#include <cstddef>
#include <memory>
#include <utility>

struct State{
    std::array<double,3> position{};
    std::array<double,3> vitesse{};
};

class Command{

    public:

        virtual std::array<double,3> getCommand(const State& state, const State& cible, double dt) const = 0;

        virtual ~Command() = default;
};

class Proportionnal : public Command {

    public:

        Proportionnal(double k) : kp(k) {};

        std::array<double,3> getCommand(const State& state, const State& cible, double dt) const override {
            double error_x = cible.position[0] - state.position[0];
            double error_y = cible.position[1] - state.position[1];
            double error_z = cible.position[2] - state.position[2];

            

            std::array<double,3> command;

            command = {kp*error_x,kp*error_y,kp*error_z};

            return command;
        };


    private:

        double kp = 0;

};

class BangBang : public Command {

    public:

        BangBang(double force) : force_max(force){};

        std::array<double,3> getCommand(const State& state, const State& cible, double dt) const override {
            double error_x = cible.position[0] - state.position[0];
            double error_y = cible.position[1] - state.position[1];
            double error_z = cible.position[2] - state.position[2];

            std::array<double,3> command;

            if (error_x < 0 ) {command[0] = -force_max;
            }
            else {
                command[0] = force_max;
            }

            if (error_y < 0 ) {
                command[1] = -force_max;
            }
            else {
                command[1] = force_max;
            }

            if (error_z < 0 ) {
                command[2] = -force_max;
            }

            else {
                command[2] = force_max;
            }

            return command;
        }

    private:

        double force_max = 0;

};

class Actioner {
    public :

        Actioner(std::unique_ptr<Command> test) : command(std::move(test)) {};

        std::array<double,3> step(const State& actuel, const State& cible, double dt) const{
            return this->command->getCommand(actuel, cible, dt);
        }

        void changeCommand(std::unique_ptr<Command> test){
            this->command = std::move(test);

        }

    private:

        std::unique_ptr<Command> command;

};



  

