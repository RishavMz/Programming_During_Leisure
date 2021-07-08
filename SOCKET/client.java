import java.net.*;
import java.io.*;
public class client
{
    public static void main(String[] args) {
        try {
            // Creating a socket and attaching it to localhost port 5000
            Socket sock = new Socket("127.0.0.1",5000);
            // Recieve input stream recieved by socket
            InputStream in = sock.getInputStream();
            // Buffereader to read data from input stream
            BufferedReader bin = new BufferedReader(new InputStreamReader(in));
            String line;
            while ( (line = bin.readLine()) != null)
                // Output recieved data
                System.out.println(line) ;
            sock.close() ;
        }
        catch (IOException ioe) {
            System.err.println(ioe) ;
        }
    }
}