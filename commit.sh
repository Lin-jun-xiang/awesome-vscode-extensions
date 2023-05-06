LATEST_COMMIT_MSG=$(git show -s --format='%s')

changed_files=$(git diff --name-only)

echo "You auto changed $changed_files"

if [[ $changed_files =~ "README" ]]; then
    if [[ "$LATEST_COMMIT_MSG" != "Auto-translate README" ]]; then
        echo "Commit..."
        git add $(git diff --name-only)
        git commit -m "Auto-translate README"
        git push
    fi
fi
