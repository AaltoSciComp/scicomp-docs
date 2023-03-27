# Return a random page - perhaps useful for a random social media
# post.

cd $(dirname $0)/..

find . -regextype posix-extended -iregex '.*\.(rst|md)$' | sort -R | head -3
