package com.virtualsecretary.virtual_secretary.entity;

import com.virtualsecretary.virtual_secretary.enums.Degree;
import com.virtualsecretary.virtual_secretary.enums.Role;
import jakarta.persistence.*;
import lombok.*;
import lombok.experimental.FieldDefaults;

import java.time.LocalDate;
import java.util.Base64;
import java.util.Set;


@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
@FieldDefaults(level = AccessLevel.PRIVATE)
@Entity
@Table(name = "employee")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    Long id;

    @ManyToOne
    @JoinColumn(name = "department_id")
    Department department;
    @Column(nullable = false, unique = true)
    String employeeCode;
    @Column(nullable = false)
    String name;
    @Column(nullable = false)
    String password;
    @Column(nullable = false)
    LocalDate dob;
    @Column(unique = true)
    String phoneNumber;
    @Enumerated(EnumType.STRING)
    @Column(nullable = false)
    Degree degree;
    @Column(unique = true)
    String identification;
    String address;
    String bankName;
    String bankNumber;
    @Column(nullable = false, unique = true)
    String email;
    @Lob
    String img;
    @Enumerated(EnumType.STRING)
    @Column(nullable = false)
    Role role;

}
