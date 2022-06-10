package com.siszero.app.dto;

import com.google.gson.annotations.SerializedName;

public class RecommendedBook {
    @SerializedName("id")
    private int id;
    @SerializedName("title")
    private String title;
    @SerializedName("writer")
    private String writer;
    @SerializedName("content")
    private String content;
    @SerializedName("image")
    private String image;
    @SerializedName("book_id")
    private int book_id;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getWriter() {
        return writer;
    }

    public void setWriter(String writer) {
        this.writer = writer;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }

    public int getBook_id() {
        return book_id;
    }

    public void setBook_id(int book_id) {
        this.book_id = book_id;
    }
}
