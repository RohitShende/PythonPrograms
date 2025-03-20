package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class DemoApplication {

	/**
	 * Serves as the entry point for the Spring Boot application.
	 *
	 * <p>Initializes and launches the application using the provided command-line arguments.</p>
	 *
	 * @param args the command-line arguments used for configuring the application context
	 */
	public static void main(String[] args) {
		SpringApplication.run(DemoApplication.class, args);
	}

}
