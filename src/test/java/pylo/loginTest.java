package pylo;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import org.testng.Assert;
import org.testng.annotations.Test;

public class loginTest {
	 @Test
	    public void executePythonLoginTest() {
	        try {
	            System.out.println("Starting Python Login Automation execution via Java ProcessBuilder...");
	            
	            // Invoke the Python page script inside your workspace directory
	            ProcessBuilder processBuilder = new ProcessBuilder("python", "webpage/page.py");
	            processBuilder.redirectErrorStream(true);
	            
	            Process process = processBuilder.start();
	            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
	            
	            String line;
	            while ((line = reader.readLine()) != null) {
	                System.out.println("[Python Out]: " + line);
	            }
	            
	            int exitCode = process.waitFor();
	            System.out.println("Python execution completed with Exit Code: " + exitCode);
	            
	            // Assert that the script returned a 0 (Successful exit code)
	            Assert.assertEquals(exitCode, 0, "The Python automation script failed to log in successfully.");
	            
	        } catch (Exception e) {
	            e.printStackTrace();
	            Assert.fail("Exception occurred while trying to run Python automation script: " + e.getMessage());
	        }
	    }

}
