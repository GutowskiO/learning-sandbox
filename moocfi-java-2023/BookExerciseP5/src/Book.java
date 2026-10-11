public class Book {
    private String author;
    private String name;
    private int pages;
    public Book(String author, String name, int pages) {
        this.author = author;
        this.name = name;
        this.pages = pages;
    }

    public String getName() {
        return this.name;
    }

    public String getAuthor() {
        return this.author;
    }

    public int getPages() {
        return this.pages;
    }

    @Override
    public String toString() {
        return this.author + ", " + this.name + ", " + this.pages + " pages";
    }
}
