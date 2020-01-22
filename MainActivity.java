package com.androidsrc.client;

import android.os.Bundle;
import android.app.Activity;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.VideoView;
public class MainActivity extends Activity {

	ImageView response;
	VideoView videoresponse;
	EditText addressedittext, portedittext,Authenticationtext;
	Button buttonConnect, buttonClear,buttonDetails,buttonNo,buttonYes,buttonImage;
	TextView detailsTextView;
	int i=1;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		//setContentView(R.layout.activity_video);
		addressedittext = (EditText) findViewById(R.id.ipaddressText);
		portedittext = (EditText) findViewById(R.id.portText);
		buttonConnect = (Button) findViewById(R.id.connectionbutton);
		buttonClear = (Button) findViewById(R.id.clearbutton);
		response = (ImageView) findViewById(R.id.testimageview);
		buttonDetails=(Button)findViewById(R.id.displaydetails);
		detailsTextView=(TextView)findViewById(R.id.imagedetails);
		Authenticationtext=(EditText)findViewById(R.id.authentication);
		buttonNo=(Button)findViewById(R.id.nobutton);
		buttonYes=(Button)findViewById(R.id.yesbutton);
        buttonImage=(Button)findViewById(R.id.image);
		detailsTextView.setVisibility(View.INVISIBLE);
		response.setVisibility(View.INVISIBLE);
		buttonDetails.setVisibility(View.INVISIBLE);
		buttonNo.setVisibility(View.INVISIBLE);
		buttonYes.setVisibility(View.INVISIBLE);
		Authenticationtext.setVisibility(View.INVISIBLE);

			buttonConnect.setOnClickListener(new OnClickListener() {

				@Override
				public void onClick(View arg0) {

					Client myClient = new Client(addressedittext.getText()
							.toString(), Integer.parseInt(portedittext
							.getText().toString()), response, buttonDetails);
					myClient.execute();

				}
			});

		buttonDetails.setOnClickListener(new OnClickListener() {

			@Override
			public void onClick(View arg0) {
				Authenticationtext.setVisibility(View.VISIBLE);
				buttonYes.setVisibility(View.VISIBLE);
				buttonNo.setVisibility(View.VISIBLE);
				DisplayDetails myClient1 = new DisplayDetails(addressedittext.getText()
						.toString(), Integer.parseInt(portedittext
						.getText().toString()), detailsTextView);
				myClient1.execute();
			}
		});


		buttonNo.setOnClickListener(new OnClickListener() {

			@Override
			public void onClick(View arg0) {
				uploadauthenticationstatustoserver myClient2=new uploadauthenticationstatustoserver(addressedittext.getText()
						.toString(), Integer.parseInt(portedittext
						.getText().toString()),"nobutton",buttonNo,buttonYes);
				myClient2.execute();
			}
		});

		buttonYes.setOnClickListener(new OnClickListener() {

			@Override
			public void onClick(View arg0) {
				uploadauthenticationstatustoserver myClient2=new uploadauthenticationstatustoserver(addressedittext.getText()
						.toString(), Integer.parseInt(portedittext
						.getText().toString()),"yesbutton",buttonNo,buttonYes);
				myClient2.execute();
			}
		});



		buttonClear.setOnClickListener(new OnClickListener() {

			@Override
			public void onClick(View v) {
				response.setImageAlpha(0);
				detailsTextView.setVisibility(View.INVISIBLE);
				Authenticationtext.setVisibility(View.INVISIBLE);
				buttonYes.setVisibility(View.INVISIBLE);
				buttonNo.setVisibility(View.INVISIBLE);
			}
		});
	}

}
