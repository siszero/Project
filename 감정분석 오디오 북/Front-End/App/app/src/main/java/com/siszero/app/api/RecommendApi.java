package com.siszero.app.api;

import com.siszero.app.dto.RecommendedBook;

import java.util.List;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.DELETE;
import retrofit2.http.GET;
import retrofit2.http.PATCH;
import retrofit2.http.POST;
import retrofit2.http.Path;
import retrofit2.http.Query;

public interface RecommendApi {

    @GET("user/recommendedbook/{book_pk}")
    Call<List<RecommendedBook>> getRecommenedBook(@Path("book_pk") int book_pk);
}
