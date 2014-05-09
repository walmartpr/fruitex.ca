import java.io.*;
import java.net.URL;

class image {
public static void main(String args[]) throws Exception {
	BufferedReader br = new BufferedReader(new FileReader(args[0]));
	String line = "";
	while ((line = br.readLine()) != null) {
		System.out.println(line.substring(17,line.length()));
	    URL url = new URL(line.substring(17,line.length()));
	    InputStream in = new BufferedInputStream(url.openStream());
	    ByteArrayOutputStream out = new ByteArrayOutputStream();
	    byte[] buf = new byte[1024];
	    int n = 0;	
	    while (-1 != (n = in.read(buf))) {
   	    	out.write(buf, 0, n);
    	}
    	out.close();
    	in.close();
    	byte[] response = out.toByteArray();
	
	    FileOutputStream fos = new FileOutputStream("./" + line.substring(0,16) + ".JPG");
	    fos.write(response);
	    fos.close();
	}
	br.close();
}}
