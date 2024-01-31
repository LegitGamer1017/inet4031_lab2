#include <stdio.h>

int main() {
    char* users[] = {"User1", "User2", "User3"};

    printf("C says: Hello, World!\n");
    for (int i = 0; i < 3; i++) {
        printf("%s\n", users[i]);
    }

    return 0;
}

