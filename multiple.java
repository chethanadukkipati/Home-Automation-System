package com.androidsrc.client;
import android.os.AsyncTask;
import android.util.Log;
import android.view.View;
import java.io.ByteArrayOutputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.net.Socket;
import java.net.UnknownHostException;
import android.widget.Button;
import android.graphics.Color;

public class multiple extends AsyncTask<Void, Void, Void> {

    String destinationAddress;
    int destinationPort;
    String output;
    byte[] b;
    Button example,buttonConnect,buttonNo,buttonDetails;
    String id="";
    multiple(String address, int port,Button example) {
        Log.d("con", "yes");
        destinationAddress = address;
        destinationPort = port;
        this.example=example;
    }


    @Override
    protected Void doInBackground(Void... arg0) {

        Socket socket = null;

        try {
            socket = new Socket(destinationAddress, destinationPort);
            Log.d("soc upload", "connected");

            Log.d("soc upload", socket.getLocalAddress().toString());
            ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream(
                    1024);
            byte[] buffer = new byte[1024];
            OutputStream outputStream = socket.getOutputStream();

            DataOutputStream dataOutputStream = new DataOutputStream(outputStream);
            if (id.equals("Connect to the server...")) {
                dataOutputStream.write('0');
                output="1";
            }
            else if (id.equals("Display details")){
                dataOutputStream.write('1');
                output="2";
            }
            else{
                dataOutputStream.write('2');
                output="3";
            }

            dataOutputStream.flush();
            Log.d("data",String.valueOf(dataOutputStream));
            dataOutputStream.close();
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
        if(output=="1")
        {
          example=buttonConnect;
        }
        else if(output=="2")
        {
            example=buttonDetails;
        }
        else if(output=="3")
        {
            example=buttonNo;
        }



    }

}
