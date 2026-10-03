public class Book {
    private String title;
    private int publicationYear;
    private int pages;

    public Book(String title, int pages, int publicationYear) {
        this.title = title;
        this.publicationYear = publicationYear;
        this.pages = pages;
    }

    public String getTitle() {
        return this.title;
    }

    @Override
    public String toString(){
        return this.title + ", " + this.pages + " pages, " + this.publicationYear;
    }
}
