#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
    if (argc < 2) return 1;
    
    // Simulate a secure signing process
    printf("HMAC-SHA256-SIG:");
    for(int i = 0; i < strlen(argv[1]); i++) {
        printf("%02x", argv[1][i] ^ 0xAA);
    }
    return 0;
}