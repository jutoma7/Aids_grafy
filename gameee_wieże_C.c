#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

#define N_MAX 100

bool is_valid(int n, int matrix[N_MAX][N_MAX], int row, int col, int value) {
    // Sprawdź, czy wartość jest unikalna w wierszu i kolumnie
    for (int i = 0; i < n; i++) {
        if (matrix[row][i] == value || matrix[i][col] == value) {
            return false;
        }
    }
    return true;
}

bool solve_matrix(int n, int matrix[N_MAX][N_MAX], int row, int col) {
    if (row == n) {
        return true; // Jeśli doszliśmy do końca macierzy, zwróć sukces
    }

    for (int value = 1; value <= n; value++) {
        if (is_valid(n, matrix, row, col, value)) {
            matrix[row][col] = value;

            // Przejdź do następnej komórki w macierzy
            int next_row = row;
            int next_col = (col + 1) % n;
            if (next_col == 0) {
                next_row++;
            }

            // Rekurencyjnie rozwiązuj resztę macierzy
            if (solve_matrix(n, matrix, next_row, next_col)) {
                return true;
            }

            // Jeśli nie można znaleźć rozwiązania, cofnij się i spróbuj inną wartość
            matrix[row][col] = 0;
        }
    }

    return false; // Nie można znaleźć rozwiązania dla aktualnej konfiguracji
}

void generate_unique_matrix(int n, int matrix[N_MAX][N_MAX]) {
    // Inicjalizuj generator liczb pseudolosowych
    srand(time(NULL));
    
    // Rozpocznij rekurencyjne rozwiązywanie macierzy z pierwszej komórki
    solve_matrix(n, matrix, 0, 0);
}


void check_pl(int n, int matrix[N_MAX][N_MAX], int widoki[N_MAX]) {
    int i, j;
    
    for (i = 0; i < n; i++) {
        int widok = 0;
        int max_wysokosc = 0;
        for (j = 0; j < n; j++) {
            if (max_wysokosc < matrix[i][n - 1 - j]) {
                widok++;
                max_wysokosc = matrix[i][n - 1 - j];
            }
        }
        widoki[i] = widok;
    }
}

void check_lp(int n, int matrix[N_MAX][N_MAX], int widoki[N_MAX]) {
    int i, j;
    
    for (i = 0; i < n; i++) {
        int widok = 0;
        int max_wysokosc = 0;
        for (j = 0; j < n; j++) {
            if (max_wysokosc < matrix[i][j]) {
                widok++;
                max_wysokosc = matrix[i][j];
            }
        }
        widoki[i] = widok;
    }
}

void check_gd(int n, int matrix[N_MAX][N_MAX], int widoki[N_MAX]) {
    int i, j;
    
    for (i = 0; i < n; i++) {
        int widok = 0;
        int max_wysokosc = 0;
        for (j = 0; j < n; j++) {
            if (max_wysokosc < matrix[n - 1 - j][i]) {
                widok++;
                max_wysokosc = matrix[n - 1 - j][i];
            }
        }
        widoki[i] = widok;
    }
}

void check_dg(int n, int matrix[N_MAX][N_MAX], int widoki[N_MAX]) {
    int i, j;
    
    for (i = 0; i < n; i++) {
        int widok = 0;
        int max_wysokosc = 0;
        for (j = 0; j < n; j++) {
            if (max_wysokosc < matrix[j][i]) {
                widok++;
                max_wysokosc = matrix[j][i];
            }
        }
        widoki[i] = widok;
    }
}

int main() {
    srand(time(NULL));
    int n;
    printf("Enter the size of the matrix: ");
    scanf("%d", &n);
    
    int matrix_rozwiazanie[N_MAX][N_MAX] = {{0}};
    
    generate_unique_matrix(n, matrix_rozwiazanie);
    
    int i;
    for (i = 0; i < n; i++) {
        while (matrix_rozwiazanie[i][i] == 0) {
            generate_unique_matrix(n, matrix_rozwiazanie);
        }
    }
    
    int widoki_lp[N_MAX], widoki_pl[N_MAX], widoki_gd[N_MAX], widoki_dg[N_MAX];
    
    check_lp(n, matrix_rozwiazanie, widoki_lp);
    check_pl(n, matrix_rozwiazanie, widoki_pl);
    check_gd(n, matrix_rozwiazanie, widoki_gd);
    check_dg(n, matrix_rozwiazanie, widoki_dg);
    
    printf("  ");
    for (i = 0; i < n; i++) {
        printf("%d ", widoki_dg[i]);
    }
    printf("\n");
    
    for (i = 0; i < n; i++) {
        int j;
        printf("%d: ", widoki_lp[i]);
        for (j = 0; j < n; j++) {
            printf("%d ", matrix_rozwiazanie[i][j]);
        }
        printf(": %d\n", widoki_pl[i]);
    }
    
    printf("  ");
    for (i = 0; i < n; i++) {
        printf("%d ", widoki_gd[i]);
    }
    printf("\n");
    
    return 0;
}
