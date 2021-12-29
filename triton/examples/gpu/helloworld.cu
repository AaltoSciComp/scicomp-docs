#include "stdio.h"

__global__ void cuda_hello(int* a){
        // blockIdx has values between 0 and 4
        printf("Hello World from GPU a[%d]=%d \n", blockIdx.x, a[blockIdx.x]);
}

int main(void) {
        int* d_a;

        // Allocates an array of 5 integers
        cudaMalloc(&d_a, 5*sizeof(int));

        // Runs 5 instances of kernel cuda_hello in parallel
        cuda_hello<<<5, 1>>>(d_a); 

        // This is needed for the printf in the kernel to display
        cudaDeviceSynchronize();

        printf("Hello from outside GPU\n");
        return 0;
}
