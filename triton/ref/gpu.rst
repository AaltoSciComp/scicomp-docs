.. csv-table::
   :delim: |

   Card          | total amount   | nodes        | architecture   | compute threads per GPU   | memory per card   | CUDA compute capability  | Slurm feature name  | Slurm gres name
   Tesla K80\*   | 12             | gpu[20-22]   | Kepler         | 2x2496                    | 2x12GB            | 3.7                      | ``kepler``          | ``teslak80``
   Tesla P100    | 20             | gpu[23-27]   | Pascal         | 3854                      | 16GB              | 6.0                      | ``pascal``          | ``teslap100``
   Tesla V100    | 40             | gpu[28-37]   | Volta          | 5120                      | 32GB              | 7.0                      | ``volta``	   | ``v100``
   Tesla V100    | 16             | dgx[01-02]   | Volta          | 5120                      | 16GB              | 7.0                      | ``volta``	   | ``v100``
