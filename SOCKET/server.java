import java.net.*;
import java.io.*;
public class server
{
    public static void main(String[] args) {
        final int PORT = 5000;
        try {
            // Creating a server socket to listen to client requests and attaching to given port
            ServerSocket sock = new ServerSocket(PORT);
            while (true) {
                // Accepting requests from clients
                Socket client = sock.accept();
                // Printwriter to write response to the client
                PrintWriter pout = new PrintWriter(client.getOutputStream() , true);
                // Sending a response
                pout.println("Hello from server");
                // Stop accepting further responses from that client
                client.close() ;
            }
        }
        catch (IOException ioe) {
            System.err.println(ioe) ;
        }
    }
}