package com.siszero.app.api;

import com.siszero.app.dto.Book;
import java.lang.String;
import java.util.List;

import retrofit2.Call;
import retrofit2.http.GET;
import retrofit2.http.Path;

public interface BookApi {
    @GET("user/book/{id}")
    Call<List<Book>> getBook(@Path("id") int id);
//    @GET("user/book/{emotion}")
//    Call<Book> getBook(@Path("emotion") String emotion);
}