package com.cosmos.oh_spring263.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * @author cosmos
 */
@RestController
public class HelloWorld {
    @GetMapping("/helloworld")
    public String helloWorld(){
        return "HelloWorld";
    }

}
