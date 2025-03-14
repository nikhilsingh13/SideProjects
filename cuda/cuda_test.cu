# include <stdio.h>

// CUDA kernel function
__global__ void helloFromGPU(){
    printf("Hello world! GPU working. Thread ID: %d\n", threadIdx.x);
}

int main() {
    printf("This is your CPU speaking....\n");

    // Launching kernel with 1 block and 10 threads
    helloFromGPU<<<1, 10>>>();

    // Wait for GPU to finish before exiting
    cudaDeviceSynchronize();

    return 0;
}