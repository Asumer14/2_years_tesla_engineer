#!/bin/bash

echo "🚀 Starting daily commit..."

cd ~/Documents/2_years_tesla_engineer

git st

git add .

echo "Enter commit message:"
read commit_msg

git commit -m "$commit_msg"

git push

echo "✅ Daily commit completed!"