#!/bin/bash

# Push Fair Case splash to GitHub
# This script syncs the faircase-splash folder to a separate git repo and force-pushes it

set -e  # Exit on error

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Configuration
REPO_DIR="$HOME/getafaircase-repo"
SOURCE_DIR="$(cd "$(dirname "$0")/final-website" && pwd)"
REMOTE_URL="https://github.com/davisballard/getafaircase-6178.git"
BRANCH="main"

echo -e "${BLUE}🚀 Push Fair Case to GitHub${NC}"
echo "=================================="
echo ""

# Create repo directory if it doesn't exist
if [ ! -d "$REPO_DIR" ]; then
    echo -e "${BLUE}📁 Creating repo directory...${NC}"
    mkdir -p "$REPO_DIR"
    cd "$REPO_DIR"
    git init
    git remote add origin "$REMOTE_URL"
    echo -e "${GREEN}✓ Repo initialized${NC}"
else
    cd "$REPO_DIR"
    # Make sure remote is set correctly
    if ! git remote get-url origin &>/dev/null; then
        git remote add origin "$REMOTE_URL"
    fi
fi

# Sync files from faircase-splash to repo
echo -e "${BLUE}📦 Syncing files...${NC}"
rsync -av --delete \
    --exclude '.git' \
    --exclude '.DS_Store' \
    --exclude '*.pyc' \
    --exclude '__pycache__' \
    "$SOURCE_DIR/" "$REPO_DIR/"

echo -e "${GREEN}✓ Files synced${NC}"

# Git operations
echo -e "${BLUE}📝 Committing changes...${NC}"
git add -A

if git diff --staged --quiet; then
    echo -e "${GREEN}✓ No changes to commit${NC}"
else
    COMMIT_MSG="Update Fair Case splash - $(date '+%Y-%m-%d %H:%M:%S')"
    git commit -m "$COMMIT_MSG"
    echo -e "${GREEN}✓ Changes committed${NC}"
fi

# Force push to remote
echo -e "${BLUE}🚀 Force pushing to GitHub...${NC}"
git push --force origin "$BRANCH"

echo ""
echo -e "${GREEN}✅ Successfully pushed to GitHub!${NC}"
echo -e "${BLUE}Repository: $REMOTE_URL${NC}"
