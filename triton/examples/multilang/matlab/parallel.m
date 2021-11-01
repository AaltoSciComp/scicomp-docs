initParPool()
% Create matrices to invert
mat = rand(1000,1000,6);

parfor i=1:size(mat,3)
    invMats(:,:,i) = inv(mat(:,:,i))
end
% And now, we proceed to build the averages of each set of inverted matrices
% each time leaving out one.

parfor i=1:size(invMats,3)
    usedelements = true(size(invMats,3),1)
    usedelements(i) = false
    res(:,:,i) = inv(mean(invMats(:,:,usedelements),3));
end
% end the program
exit(0)
