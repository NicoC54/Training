//global variables
#include <opencv2/opencv.hpp>

//on cree un vecteur de pointeur car les classes héritées gauss et canny nont pas forcément la meme taille que filter : un pointeur possède une taille uniforme 1 byte

class Filter {

    public:
 //attention à la syntaxe : on met virtual void (param) = 0; puis virtual destructeur
        virtual void applyFilter(cv::Mat& image) = 0;
        virtual ~Filter() = default;

};


class Gauss : public Filter {

    public:

        Gauss() = default;

         void applyFilter(cv::Mat& image) override {
            cv::GaussianBlur(image,image,size, 0);
            std::cout << "Filtre de Gauss appliqué"<<std::endl;
         }

    private: 
            
        cv::Size size(5,5);

};

class Canny : public Filter {

    public:

        Canny() = default;

        void applyFilter(cv::Mat& image) override {
            cv::Canny(image,image, low_threshold, high_threshold);
            std::cout << "Filtre de canny appliqué"<<std::endl;
        }

    private:

        int low_threshold = 50;
        int high_threshold = 150;

}

std::vector<std::shared_ptr<Filter>> filters; 
std::mutex ImageMutex;

cv::Mat CapturedImage;
cv::Mat PassationImage;
cv::Mat TreatmentImage;

cv::VideoCapture cap;


void CaptureImage(){

    cap.open(0);

    while(true){

        cap >> CapturedImage;

        if (!CapturedImage.empty()){
            std::lock_guard<std::mutex> lock(ImageMutex);
            PassationImage = CapturedImage.clone();
        }
        }

}


void ApplyFilter(){

    auto Gauss = std::make_shared<Gauss>();
    auto Canny = std::make_shared<Canny>();
    filters.push_back(Gauss);
    filters.push_back(Canny);


    while(true){

        {
        std::lock_guard<std::mutex> lock(ImageMutex);

        if (!PassationImage.empty()){
            TreatmentImage = PassationImage.clone();
        }
        }

        for (std::shared_ptr<Filter> filter : filters) {
            filter -> applyFilter(TreatmentImage);
        }

        cv::imshow("image filtered", TreatmentImage);
        cv::waitKey(0);


        }

    }


int main(){

    std::thread ThreadCaptureImage(CaptureImage);
    std::thread ThreadApplyFilter(ApplyFilter);

    ThreadCaptureImage.join();
    ThreadApplyFilter.join();


    return 0;
}