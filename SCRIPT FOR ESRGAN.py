!wget https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.5.0/realesrgan-ncnn-vulkan-20220424-ubuntu.zip
!unzip -o realesrgan-ncnn-vulkan-20220424-ubuntu.zip
!apt-get update
!apt-get install -y libvulkan1 mesa-vulkan-drivers
!chmod +x realesrgan-ncnn-vulkan
!./realesrgan-ncnn-vulkan -h
