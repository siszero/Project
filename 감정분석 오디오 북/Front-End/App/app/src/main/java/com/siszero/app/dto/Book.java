package com.siszero.app.dto;

import com.google.gson.annotations.SerializedName;

public class Book {
    @SerializedName("id")
    private int id;
    @SerializedName("category")
    private String category;
    @SerializedName("title")
    private String title;
    @SerializedName("content")
    private String content;
    @SerializedName("writer")
    private String writer;
    @SerializedName("image")
    private String image;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public String getWriter() {
        return writer;
    }

    public void setWriter(String writer) {
        this.writer = writer;
    }

    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }
}
