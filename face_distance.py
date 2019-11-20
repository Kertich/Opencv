import face_recognition


# Load a sample picture and learn how to recognize it.
obama_image = face_recognition.load_image_file("obama.jpg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

# Create arrays of known face encodings
known_face_encodings = [obama_face_encoding]


# Load an image with an unknown face
unknown_image = face_recognition.load_image_file("obama_unknown.jpg")
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

# Calculate face distance
face_distances = face_recognition.face_distance(known_face_encodings, unknown_face_encoding)

print("The face has a distance of {:.2} from the face in unknown".format(face_distances[0]))
print("With cutoff of less than 0.6, Match is {}".format(face_distances[0] < 0.6))
