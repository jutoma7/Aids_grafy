#include "raylib.h"

#define SIZE 6

// Function to draw the grid and the frame
void DrawGrid(int grid[SIZE][SIZE], int top[SIZE], int bottom[SIZE], int left[SIZE], int right[SIZE]) {
    int cellSize = 50;
    int frameOffset = 100;

    // Draw the grid with numbers
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            Rectangle cell = { frameOffset + j * cellSize, frameOffset + i * cellSize, cellSize, cellSize };
            DrawRectangleLinesEx(cell, 2, BLACK);
            if (grid[i][j] != 0) {
                DrawText(TextFormat("%d", grid[i][j]), cell.x + 20, cell.y + 10, 20, BLACK);
            }
        }
    }

    // Draw the frame with visibility numbers
    for (int i = 0; i < SIZE; i++) {
        // Top frame
        if (top[i] != 0) {
            DrawText(TextFormat("%d", top[i]), frameOffset + i * cellSize + 20, frameOffset - cellSize / 2 + 10, 20, BLACK);
        }

        // Bottom frame
        if (bottom[i] != 0) {
            DrawText(TextFormat("%d", bottom[i]), frameOffset + i * cellSize + 20, frameOffset + SIZE * cellSize + cellSize / 2 - 10, 20, BLACK);
        }

        // Left frame
        if (left[i] != 0) {
            DrawText(TextFormat("%d", left[i]), frameOffset - cellSize / 2 + 10, frameOffset + i * cellSize + 10, 20, BLACK);
        }

        // Right frame
        if (right[i] != 0) {
            DrawText(TextFormat("%d", right[i]), frameOffset + SIZE * cellSize + cellSize / 2 - 10, frameOffset + i * cellSize + 10, 20, BLACK);
        }
    }
}

// Function to check if the grid is correct
bool CheckGrid(int grid[SIZE][SIZE], int top[SIZE], int bottom[SIZE], int left[SIZE], int right[SIZE]) {
    // Check each row and column for uniqueness and visibility constraints
    for (int i = 0; i < SIZE; i++) {
        // Check rows for uniqueness
        bool rowCheck[SIZE] = { false };
        for (int j = 0; j < SIZE; j++) {
            int val = grid[i][j];
            if (val == 0 || rowCheck[val - 1]) return false; // Duplicates or empty cells
            rowCheck[val - 1] = true;
        }

        // Check columns for uniqueness
        bool colCheck[SIZE] = { false };
        for (int j = 0; j < SIZE; j++) {
            int val = grid[j][i];
            if (val == 0 || colCheck[val - 1]) return false; // Duplicates or empty cells
            colCheck[val - 1] = true;
        }

        // Check visibility constraints
        int maxSeen = 0, seenCount = 0;
        // Check top to bottom
        for (int j = 0; j < SIZE; j++) {
            if (grid[j][i] > maxSeen) {
                maxSeen = grid[j][i];
                seenCount++;
            }
        }
        if (seenCount != top[i]) return false;

        // Check bottom to top
        maxSeen = 0;
        seenCount = 0;
        for (int j = SIZE - 1; j >= 0; j--) {
            if (grid[j][i] > maxSeen) {
                maxSeen = grid[j][i];
                seenCount++;
            }
        }
        if (seenCount != bottom[i]) return false;

        // Check left to right
        maxSeen = 0;
        seenCount = 0;
        for (int j = 0; j < SIZE; j++) {
            if (grid[i][j] > maxSeen) {
                maxSeen = grid[i][j];
                seenCount++;
            }
        }
        if (seenCount != left[i]) return false;

        // Check right to left
        maxSeen = 0;
        seenCount = 0;
        for (int j = SIZE - 1; j >= 0; j--) {
            if (grid[i][j] > maxSeen) {
                maxSeen = grid[i][j];
                seenCount++;
            }
        }
        if (seenCount != right[i]) return false;
    }
    return true;
}

// Initialize the puzzle grid and frame
void InitializeGrid(int grid[SIZE][SIZE], int top[SIZE], int bottom[SIZE], int left[SIZE], int right[SIZE]) {
    // Example grid (0 represents an empty cell)
    int exampleGrid[SIZE][SIZE] = {
        {0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0}
    };

    // Example visibility numbers
    int exampleTop[SIZE] = {2, 3, 1, 4, 2, 3};
    int exampleBottom[SIZE] = {1, 2, 2, 3, 2, 1};
    int exampleLeft[SIZE] = {3, 1, 2, 4, 2, 1};
    int exampleRight[SIZE] = {2, 2, 3, 1, 2, 3};

    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            grid[i][j] = exampleGrid[i][j];
        }
    }

    for (int i = 0; i < SIZE; i++) {
        top[i] = exampleTop[i];
        bottom[i] = exampleBottom[i];
        left[i] = exampleLeft[i];
        right[i] = exampleRight[i];
    }
}

int main() {
    InitWindow(800, 600, "Skyscrapers Puzzle Game");

    int grid[SIZE][SIZE];
    int top[SIZE], bottom[SIZE], left[SIZE], right[SIZE];
    InitializeGrid(grid, top, bottom, left, right);

    int selectedRow = -1;
    int selectedCol = -1;

    bool showMessage = false;
    const char *message = "";

    SetTargetFPS(60);

    while (!WindowShouldClose()) {
        if (IsMouseButtonPressed(MOUSE_BUTTON_LEFT)) {
            Vector2 mousePosition = GetMousePosition();
            int cellSize = 50;
            int col = (mousePosition.x - 100) / cellSize;
            int row = (mousePosition.y - 100) / cellSize;
            if (col >= 0 && col < SIZE && row >= 0 && row < SIZE) {
                selectedRow = row;
                selectedCol = col;
            } else {
                selectedRow = -1;
                selectedCol = -1;
            }

            // Check if the submit button was clicked
            Rectangle submitButton = { 350, 450, 100, 40 };
            if (CheckCollisionPointRec(mousePosition, submitButton)) {
                if (CheckGrid(grid, top, bottom, left, right)) {
                    showMessage = true;
                    message = "Correct!";
                } else {
                    showMessage = true;
                    message = "Incorrect!";
                }
            }
        }

        if (selectedRow != -1 && selectedCol != -1) {
            for (int key = KEY_ONE; key <= KEY_SIX; key++) {
                if (IsKeyPressed(key)) {
                    grid[selectedRow][selectedCol] = key - KEY_ONE + 1;
                }
            }
        }

        BeginDrawing();
        ClearBackground(RAYWHITE);

        DrawGrid(grid, top, bottom, left, right);

        // Draw the submit button
        Rectangle submitButton = { 350, 450, 100, 40 };
        DrawRectangleRec(submitButton, LIGHTGRAY);
        DrawRectangleLinesEx(submitButton, 2, BLACK);
        DrawText("Submit", 370, 460, 20, BLACK);

        // Show message
        if (showMessage) {
            DrawText(message, 350, 500, 20, RED);
        }

        if (selectedRow != -1 && selectedCol != -1) {
            int cellSize = 50;
            Rectangle selectedCell = { 100 + selectedCol * cellSize, 100 + selectedRow * cellSize, cellSize, cellSize };
            DrawRectangleLinesEx(selectedCell, 4, RED);
        }

        EndDrawing();
    }

    CloseWindow();
    return 0;
}
