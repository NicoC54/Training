bool is_airspeed_safe(float airspeed, float v_stall, float v_never_exceed) {
    // Si la vitesse est trop basse (< v_stall) -> pas bon
    // Si la vitesse est trop haute (> v_never_exceed) -> pas bon
    // Sinon -> c'est bon
    bool valid = true;

    if (airspeed>v_never_exceed){
        return !valid;
    }
    if (airspeed<v_stall){
        return !valid;
    }

    return valid;
}