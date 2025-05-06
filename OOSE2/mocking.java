////////////////////////////EmailSender.java/////////////////////////////////
public interface EmailSender {
    void sendEmail(String to, String message);
}

//////////////////////NotificationService.java///////////////////////////////
public class NotificationService {
    private final EmailSender emailSender;

    public NotificationService(EmailSender emailSender) {
        this.emailSender = emailSender;
    }

    public void notify(String userEmail, String message) {
        emailSender.sendEmail(userEmail, message);
    }
}

/////////////////////////////////main.java//////////////////////////////////

import static org.mockito.Mockito.*;

public class Main {
    public static void main(String[] args) {
        // Create mock of EmailSender
        EmailSender mockEmailSender = mock(EmailSender.class);

        // Pass mock into the service
        NotificationService service = new NotificationService(mockEmailSender);

        // Call method under test
        service.notify("test@example.com", "Hello from Mockito!");

        // Verify that sendEmail was called with expected parameters
        verify(mockEmailSender).sendEmail("test@example.com", "Hello from Mockito!");

        System.out.println("Mock verified successfully.");
    }
}
