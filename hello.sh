#!/bin/bash

users=("User1" "User2" "User3")

echo "Bash says: Hello, World!"
for user in "${users[@]}"; do
    echo "$user"
done

