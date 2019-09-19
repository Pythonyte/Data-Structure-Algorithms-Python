cd /home/sumitsinghal/Data-Structure-Algorithms-Python
git status
echo "=====================Add files in Git====================="
git add .

echo "================Commit files: === $1 ======================="
git commit -m "$1"

git status

echo "====================Push changes into == $2 =========================="
git push origin "$2"
