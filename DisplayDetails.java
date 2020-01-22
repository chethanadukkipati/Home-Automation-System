package com.androidsrc.client;

import android.graphics.Color;
import android.os.AsyncTask;
import android.util.Log;
import android.view.View;
import android.widget.TextView;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.Socket;
import java.net.UnknownHostException;
import android.widget.Button;

public class DisplayDetails extends AsyncTask<Void, Void, Void> {

    String destinationAddress;
    int destinationPort;
    String outputresult="";
    String output;
    byte[] b;
    TextView textResponse;

    DisplayDetails(String address, int port,TextView textResponse) {
        destinationAddress = address;
        destinationPort = port;
        this.textResponse=textResponse;

    }


    @Override
    protected Void doInBackground(Void... arg0) {

        Socket socket = null;

        try {
            socket = new Socket(destinationAddress, destinationPort);
            Log.d("soc","connected");

            Log.d("soc",socket.getLocalAddress().toString());

            ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream(
                    1024);
            byte[] buffer = new byte[1024];

            int bytesRead;
            InputStream inputStream = socket.getInputStream();

            while ((bytesRead = inputStream.read(buffer)) != -1) {
                byteArrayOutputStream.write(buffer, 0, bytesRead);
                //Log.d("response before",response);
                Log.d("byteArrayOutputStreamb",String.valueOf(byteArrayOutputStream));
                outputresult+= byteArrayOutputStream.toString("UTF-8");
                Log.d("response after",outputresult);
                Log.d("byteArrayOutputStreama",String.valueOf(byteArrayOutputStream));
            }

            Log.d("response",outputresult);
           // outputresult.replace("null",",");
            String name=outputresult.split(",")[0];
            String distance=outputresult.split(",")[1];
            String profession=outputresult.split(",")[2];
            String relation=outputresult.split(",")[3];
            String age=outputresult.split(",")[4];
            output= "Name: "+name+"\n"+"Distance: "+distance+"\n"+"Profession:"+profession+"\n"+"Relation:"+relation+"\n"+"Age:"+age;


        } catch (UnknownHostException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } finally {
            if (socket != null) {
                try {
                    socket.close();
                } catch (IOException e) {
                    // TODO Auto-generated catch block
                    e.printStackTrace();
                }
            }
        }
        return null;
    }

    @Override
    protected void onPostExecute(Void result) {


        textResponse.setText(output);
        textResponse.setTextColor(Color.RED);
        textResponse.setTextAlignment(View.TEXT_ALIGNMENT_CENTER);
        textResponse.setTextSize(20);
        textResponse.setVisibility(View.VISIBLE);



    }

}
