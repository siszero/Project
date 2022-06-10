package com.siszero.app;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;

import android.widget.ImageView;
import android.widget.TextView;

import com.siszero.app.api.BookApi;
import com.siszero.app.api.RecommendApi;
import com.siszero.app.dto.Book;
import com.siszero.app.dto.RecommendedBook;

import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class RecommendActivity extends AppCompatActivity{

    private final String BASE_URL = "http://10.0.2.2:8000/api/";
    private RecommendApi recommendApiAPI;

    private TextView textView1;
    private TextView textView2;
    private TextView textView3;
    private TextView textView4;

    private ImageView imageView1;
    private ImageView imageView2;
    private ImageView imageView3;
    private ImageView imageView4;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_recommend);

        imageView1 = findViewById(R.id.bookImage1);
        imageView2 = findViewById(R.id.bookImage2);
        imageView3 = findViewById(R.id.bookImage3);
        imageView4 = findViewById(R.id.bookImage4);

        textView1 = findViewById(R.id.booktitle1);
        textView2 = findViewById(R.id.booktitle2);
        textView3 = findViewById(R.id.booktitle3);
        textView4 = findViewById(R.id.booktitle4);

        initMyAPI(BASE_URL);

        Call<List<RecommendedBook>> getCall = recommendApiAPI.getRecommenedBook(BookActivity.bk_id);
        getCall.enqueue(new Callback<List<RecommendedBook>>() {
            @Override
            public void onResponse(Call<List<RecommendedBook>> call, Response<List<RecommendedBook>> response) {
                if (response.isSuccessful()) {
                    List<RecommendedBook> mList = response.body();
                    System.out.println("mList"+mList);

//                    String result = "";
//                    for( RecommendedBook rb : mList){
//                        result += rb.getTitle()+" "+rb.getWriter();
//                    }
//
//                    textView.setText(result);
//                    System.out.println("result"+result);

                    // 네 권 책
                    String imageName1 = mList.get(0).getImage();
                    imageView1.setImageResource(getResources().getIdentifier("@drawable/"+imageName1, "drawable",getPackageName() ));

                    String result1 = mList.get(0).getTitle();
                    textView1.setText("[ " + result1 + " ]");

                    System.out.println("imageView1" + imageName1);

                    String imageName2 = mList.get(1).getImage();
                    imageView2.setImageResource(getResources().getIdentifier("@drawable/"+imageName2, "drawable",getPackageName() ));

                    String result2 = mList.get(1).getTitle();
                    textView2.setText("[ " + result2 + " ]");

                    String imageName3 = mList.get(2).getImage();
                    imageView3.setImageResource(getResources().getIdentifier("@drawable/"+imageName3, "drawable",getPackageName() ));

                    String result3 = mList.get(2).getTitle();
                    textView3.setText("[ " + result3 + " ]");

                    String imageName4 = mList.get(3).getImage();
                    imageView4.setImageResource(getResources().getIdentifier("@drawable/"+imageName4, "drawable",getPackageName() ));

                    String result4 = mList.get(3).getTitle();
                    textView4.setText("[ " + result4 + " ]");

                } else {
                    System.out.println( "Status Code : " + response.code());
                }
            }

            @Override
            public void onFailure(Call<List<RecommendedBook>> call, Throwable t) {
                System.out.println("Fail msg : " + t.getMessage());
            }
        });
    }


    private void initMyAPI(String baseUrl){
        System.out.println("initMyAPI : " + baseUrl);
        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl(baseUrl)
                .addConverterFactory(GsonConverterFactory.create())
                .build();
        recommendApiAPI = retrofit.create(RecommendApi.class);
    }
}