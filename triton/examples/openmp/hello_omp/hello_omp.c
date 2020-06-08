/* Hello World OpenMP
 *
 * Compile on Triton as:
 *   gcc -fopenmp hello_omp.c -o hello_omp
 * 
 * degtyai1, Wed, 28 May 2014 12:47:47 +0300
 * tuomiss1, Mon, 08 Jun 2020
 *
 */

#include <stdio.h>
#if defined(_OPENMP)
#include <omp.h>
#endif

int main(void) {
#if defined(_OPENMP)
#pragma omp parallel
    printf("Hello, world from thread %d.\n", omp_get_thread_num());
#else
    printf("Hello, world.\n");
#endif
  return 0;
}
