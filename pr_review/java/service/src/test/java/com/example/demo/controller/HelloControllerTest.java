 scss
import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class HelloControllerTest {

    @Test
    public void testSayHello() {
        String expected = "hello world";
        String actual = HelloController.sayHello();
        assertEquals(expected, actual);
    }
}
