#include <stdio.h>
#include <locale.h>
#include <wchar.h>
#include <stdlib.h>
#include <string.h>


void replaceBlacklisted(wchar_t* message, wchar_t backlist[][4], int backlistSize) {
    wchar_t* tokens[10];
    wchar_t* nextToken;
    wchar_t* token = wcstok_s(message, L" ", &nextToken);

    int i = 0;
    while (token != NULL && i < 10) {
        tokens[i++] = token;
        token = wcstok_s(NULL, L" ", &nextToken);
    }

    for (int j = 0; j < i; ++j) {
        bool isBlacklisted = false;
        for (int k = 0; k < backlistSize; ++k) {
            if (wcscmp(tokens[j], backlist[k]) == 0) {
                isBlacklisted = true;
                break;
            }
        }

        if (isBlacklisted)
            for (int a = 0; a < wcslen(tokens[j]); ++a)
                wprintf(L"*");
        else { wprintf(L"%ls", tokens[j]); }

        if (j < i - 1) { wprintf(L" "); }
    }
    puts("");
}

int main(void) {
    setlocale(LC_ALL, "en_US.UTF-8");

    wchar_t backlist[][4] = { L"Địt", L"Đụ" };
    wchar_t message[] = L"Địt con mẹ chúng mày!";

    replaceBlacklisted(message, backlist, sizeof(backlist) / sizeof(backlist[0]));

    return 0;
}