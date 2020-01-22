package com.androidsrc.client;

import java.io.ByteArrayOutputStream;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.net.Socket;
import java.net.UnknownHostException;
import android.os.AsyncTask;
import android.util.Log;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import java.io.File;
import java.io.FileOutputStream;
import android.os.Environment;
import android.widget.Button;
public class Client extends AsyncTask<Void, Integer, Void> {

	String destinationAddress;
	int destinationPort;
	String returnoutput="";
	byte[] b;

	ImageView imageResponse;
	Button buttonDetails;
    Bitmap bitmap;
	Client(String address, int port, ImageView imageResponse, Button buttonDetails) {
		destinationAddress = address;
		destinationPort = port;
		this.imageResponse = imageResponse;
		this.buttonDetails = buttonDetails;
	}


	@Override
	protected Void doInBackground(Void... arg0) {

		Socket socket = null;
		try {
			socket = new Socket(destinationAddress, destinationPort);
			Log.d("soc", "connected");

			Log.d("soc", socket.getLocalAddress().toString());

			ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream(
					1024);
			byte[] buffer = new byte[1024];

			int Readbyte;
			String check = "1";
			for (int i = 1; i <=9; i++) {
				InputStream inputStream = socket.getInputStream();

				while ((Readbyte = inputStream.read(buffer)) != -1) {
					byteArrayOutputStream.write(buffer, 0, Readbyte);
				}
				for (int j = 0; j < buffer.length; j++) {
					buffer[j] = 0;
				}
				buffer = new byte[1024];

				b = byteArrayOutputStream.toByteArray();
				Log.d("buffer length", String.valueOf(b.length));
				Log.d("i val", String.valueOf(i));
				Log.d("path", Environment.DIRECTORY_PICTURES);
				String storage;
				storage = Environment.getExternalStorageState();
				Log.d("state", storage);
				if (Environment.MEDIA_MOUNTED.equals(storage)) {
					File root = Environment.getExternalStorageDirectory();
					File dir = new File(root.getAbsolutePath() + "/MyappFile_New");
					Log.d("file path full", dir.getAbsolutePath());

					dir.mkdir();
					File file = new File(dir, "photo" + i + ".jpg");
					FileOutputStream fileOutputStream = new FileOutputStream(file);
					fileOutputStream.write(b);
					fileOutputStream.close();

				} else {
					Log.d("state", "not eligible");
				}
				socket.close();
				Log.d("closed", "closed");
				inputStream.close();
				byteArrayOutputStream.flush();
				byteArrayOutputStream.reset();
				publishProgress((int) i);
				if (i != 9) {
					socket = new Socket(destinationAddress, destinationPort);
					Log.d("after soc call", "soc call a");
					InputStream inputStream1 = socket.getInputStream();
					Log.d("after inp str", "after inp str");
					Readbyte = inputStream1.read(buffer);
					Log.d("bytes read", String.valueOf(Readbyte));
					byteArrayOutputStream.write(buffer, 0, Readbyte);
					returnoutput += byteArrayOutputStream.toString("UTF-8");
					byteArrayOutputStream.flush();
					byteArrayOutputStream.reset();
					Log.d("response", returnoutput);

					for (int j = 0; j < buffer.length; j++) {
						buffer[j] = 0;
					}
					buffer = new byte[1024];
					Log.d("response", returnoutput);
					if (returnoutput.equals("1")) {
						returnoutput = "";
						Log.d("wait", "wait");
						while (true) {
							Readbyte = inputStream1.read(buffer);
							byteArrayOutputStream.write(buffer, 0, Readbyte);
							returnoutput += byteArrayOutputStream.toString("UTF-8");
							if (returnoutput.equals("0")) {
								returnoutput = "";
								byteArrayOutputStream.flush();
								byteArrayOutputStream.reset();
								socket.close();
								socket = new Socket(destinationAddress, destinationPort);
								break;
							}
						}
					}

				}
			}


		} catch (UnknownHostException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			if (socket != null) {
				try {
					socket.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
		}
		return null;
	}

	protected void onProgressUpdate(Integer... progress) {
		File root = Environment.getExternalStorageDirectory();
		File dir = new File(root.getAbsolutePath() + "/MyappFile_New");
		File file = new File(dir, "photo" + progress[0] + ".jpg");
		try {
			FileInputStream fileInputStream = new FileInputStream(file);
			Bitmap bitmap = BitmapFactory.decodeStream(fileInputStream);

			fileInputStream.close();
			imageResponse.setImageBitmap(bitmap);
			imageResponse.setVisibility(View.VISIBLE);
			buttonDetails.setVisibility(View.VISIBLE);
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}


	@Override
	protected void onPostExecute(Void result) {
          //super.onPostExecute(result);
	}
}







