package com.virtualsecretary.virtual_secretary.entity;

import com.virtualsecretary.virtual_secretary.enums.MessageType;
import jakarta.persistence.*;
import lombok.*;
import lombok.experimental.FieldDefaults;

import java.io.File;
import java.time.LocalDateTime;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
@FieldDefaults(level = AccessLevel.PRIVATE)
@Entity
@Table(name = "meeting_message")
public class MeetingMessage {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    Long id;
    long chatId;
    @ManyToOne
    @JoinColumn(name = "sender_id", nullable = false)
    Member sender;

    @Column(nullable = false)
    String receive;
    @Column(nullable = false)
    MessageType type;
    @Lob
    private byte[] file;
    String fileName;
    @Lob
    @Column(nullable = false)
    String message;

    @Column(nullable = false)
    String timestamp;
}
