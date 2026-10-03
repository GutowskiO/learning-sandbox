#include <iostream>

using namespace std; //chcemy moc pisac rzseczy typu cin, cout bez przedrostka "std::"

int main() { //główna metoda programu
    int wysokosc; //deklarujemy zmienną wysokość
    
    cout << "Napisz wysokosc drzewa swiatecznego: "; //wypisujemy pytanie
    cin >> wysokosc; //input zostaje przypisany do zmiennej wysokosc

    for (int i = 0; i < wysokosc; i++) { //tworzymy pętle, która przechodzi przez wysokosc
        for (int j = 0; j < wysokosc - i - 1; j++) { //tworzymy pętle w pierwszej pętli która bedzię odpowiedzialna za spacje w drzewie
            cout << " "; //wypisujemy spacje, daną ilość razy
        }
        
        for (int k = 0; k < 2 * i + 1; k++) { //tworzymy pętle w pierwszej pętli, która będzie odpowiedzialna za ciało drzewa (*)
            cout << "*"; //wypisujemy * daną ilość razy.
        }
        
        cout << endl; //przechodzimy do nowej linii
    }
    
    for (int i = 0; i < wysokosc - 2; i++) { //tworzymy pętle odpowiedzialną za spacje w trzonie drzewa
        cout << " ";
    }
    
    cout << "| |" << endl; // wypisujemy trzon drzewa (w tym przypadku | |)
    
    return 0; //zwracamy 0, koniec programu
}