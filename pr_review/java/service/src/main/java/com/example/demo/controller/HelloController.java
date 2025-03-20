package com.example.demo.controller;


import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;


@RestController
@RequestMapping("/api/v1")
public class HelloController {

    /**
     * Returns a simple greeting message.
     *
     * <p>This method handles HTTP GET requests to the "/hello" endpoint by returning the text "hello world".</p>
     *
     * @return the greeting message "hello world"
     */
    @GetMapping("/hello")
    public String sayHello() {
        return "hello world";
    }
}
