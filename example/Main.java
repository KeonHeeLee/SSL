import java.io.*;
import java.util.Scanner;

public class Main {
    private static final String path = "C:\\Users\\user\\IdeaProjects\\SHA256\\untitled\\src\\";
    private static String inputFileName;
    private static int fileSizeHex;
    private static byte[] b;
    private static FileInputStream fis;
    private static FileOutputStream fos;

    public static void main(String[] args) throws IOException {
        inputFileName();
        initialize();
        setDigest();
        closeStreams();
    }

    private static void inputFileName(){
        System.out.println("Input File name to convert SHA256 :");
        Scanner sc = new Scanner(System.in);
        inputFileName = sc.next();
        sc.close();
    }

    private static void initialize() throws FileNotFoundException {
        String[] tokens = inputFileName.split("\\.");
        String outputFileName = tokens[0] + "_sha256." + tokens[1];

        setFileSize();
        b = new byte[fileSizeHex];

        fis = new FileInputStream(path+inputFileName);
        fos = new FileOutputStream(path+ outputFileName);
    }

    private static void setFileSize(){
        File f = new File(path+inputFileName);
        int fileSize = (int) f.length();
        fileSizeHex = getFileSizeToHex(fileSize);
        System.out.println("Original Size : "+ fileSize);
        System.out.println("Hash Array Size : "+fileSizeHex);
    }

    private static int getFileSizeToHex(int fileSize){
        if(fileSize%64 == 0)
            return fileSize;
        else {
            int mod = fileSize % 64;
            fileSize -= mod;
            fileSize += 64;
            return fileSize;
        }
    }

    private static void setDigest() throws IOException {
        int pos = 0;
        int size = 64;

        for(; pos < fileSizeHex; pos+=size){
            int n = fis.read(b, pos, size);
            if(n == -1) break;
            String temp = new String(b, pos, size);
            String hash = new SHA256().digest(temp);
            fos.write(hash.getBytes());
            System.out.println(pos+" >> "+temp + " =>" + hash);
        }
    }

    private static void closeStreams() throws IOException {
        fis.close();
        fos.close();
    }
}