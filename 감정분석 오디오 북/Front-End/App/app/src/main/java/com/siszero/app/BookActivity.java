package com.siszero.app;

import androidx.appcompat.app.AppCompatActivity;

import android.media.MediaPlayer;
import android.os.Bundle;
import android.content.Intent;

import android.app.Activity;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import com.siszero.app.api.BookApi;
import com.siszero.app.dto.Book;

import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;


public class BookActivity extends AppCompatActivity {
    public static int bk_id;
    private final String BASE_URL = "http://10.0.2.2:8000/api/";
    private BookApi bookApiAPI;

    private TextView textView;
    private ImageView imageView;
    private Button btn_move;

    MediaPlayer mediaPlayer;
    Button play;
    Button stop;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_book);

        // 책 이미지랑 책 내용 받아오기
        textView = findViewById(R.id.bookcontent);
        imageView = findViewById(R.id.bookImage);

        play=findViewById(R.id.play);
        stop=findViewById(R.id.stop);

        btn_move = findViewById(R.id.otherrecommend);
        btn_move.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(getApplicationContext(), RecommendActivity.class);
                startActivity(intent);  // 액티비티 이동
            }
        });

        initMyAPI(BASE_URL);

        // 감정 랜덤 (리스트로 안 받음)
        // Call<Book> getCall = bookApiAPI.getBook(emotion);

        // 직접 지정해서 뽑아오는 경우 (리스트로 받음)
        // 책 바꾸는 부분
        Call<List<Book>> getCall = bookApiAPI.getBook(99);       // ai 로 감정분석 한 결과가 들어와야 함
        getCall.enqueue(new Callback<List<Book>>() {
            @Override
            public void onResponse(Call<List<Book>> call, Response<List<Book>> response) {
                if (response.isSuccessful()) {
                    List<Book> mList = response.body();
                    System.out.println("mList"+mList);

                    // RecommendedActivity에서 사용해서 위에서 public으로 정의해줌
                    // Call<List<RecommendedBook>> getCall = recommendApiAPI.getRecommenedBook(BookActivity.bk_id);
                    bk_id = mList.get(0).getId();

                    String result = "";
                    result += "[ " + mList.get(0).getTitle() + " ]" + "\n" + "\n" + mList.get(0).getContent();

                    textView.setText(result);
                    System.out.println("result"+result);

                    String imageName = mList.get(0).getImage();
                    imageView.setImageResource(getResources().getIdentifier("@drawable/"+imageName, "drawable",getPackageName() ));

                } else {
                    System.out.println( "Status Code : " + response.code());
                }
            }

            @Override
            public void onFailure(Call<List<Book>> call, Throwable t) {
                System.out.println("Fail msg : " + t.getMessage());
            }
        });

        play.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // 노래 바꾸는 부분
                mediaPlayer = MediaPlayer.create(BookActivity.this, R.raw.happy);
                mediaPlayer.start();
            }
        });

        stop.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(mediaPlayer.isPlaying()){
                    mediaPlayer.stop();
                    mediaPlayer.reset();
                }
            }
        }) ;
    }
    private void initMyAPI(String baseUrl){
        System.out.println("initMyAPI : " + baseUrl);
        Retrofit retrofit = new Retrofit.Builder()
                .baseUrl(baseUrl)
                .addConverterFactory(GsonConverterFactory.create())
                .build();
        bookApiAPI = retrofit.create(BookApi.class);
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        if(mediaPlayer != null){
            mediaPlayer.release();
            mediaPlayer = null;
        }
    }
}