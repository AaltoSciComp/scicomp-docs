.. csv-table::
   :delim: |

   Card          | total amount   | nodes        | architecture   | compute threads per GPU   | memory per card   | CUDA compute capability  | Slurm feature name  | Slurm gres name
   Tesla M2090   | 22             | gpu[1-11]    | Fermi          | 512                       | 6G                | 2.0                      | ``fermi``           | ``m2090``
   Tesla M2070   | 6              | gpu[17-19]   | Fermi          | 448                       | 6G                | 2.0                      | ``fermi``           | ``m2070``
   Tesla M2050   | 10             | gpu[12-16]   | Fermi          | 448                       | 3G                | 2.0                      | ``fermi``           | ``m2050``
   Tesla K80\*   | 12             | gpu[20-22]   | Kepler         | 2x2496                    | 2x12GB            | 3.7                      | ``kepler``          | ``teslak80``
   Tesla P100    | 20             | gpu[23-27]   | Pascal         | 3854                      | 16GB              | 6.0                      | ``pascal``          | ``teslap100``
   Tesla V100    | 40             | gpu[28-37]   | Volta          | 5120                      | 32GB              | 7.0                      | ``volta``	   | ``v100``
   Tesla V100    | 16             | dgx[01-02]   | Volta          | 5120                      | 16GB              | 7.0                      | ``volta``	   | ``v100``
