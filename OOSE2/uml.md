# [UML/Class Diagrams](https://github.com/Hanif-K-Musaheb/Year-2-CompSci-Notes/blob/main/OOSE2/oose.md)
### dependency
Often times one class may make use of another class. This is known as a dependency since one class is dependent upon another class. We represent such a dependency with a dashed line with an arrow. The arrow points to the class that is depended upon.

| Feature           | Dependency            | Composition                    |
| ----------------- | --------------------- | ------------------------------ |
| Symbol            | Dashed arrow (`--->`) | Solid line with filled diamond |
| Relationship type | Uses / Knows about    | Owns / Part-of                 |
| Lifetime control  | No                    | Yes                            |
| Tightness         | Loose                 | Strong                         |
| Example           | Printer → Document    | House ♦── Room                 |


<img width="586" alt="image" src="https://github.com/user-attachments/assets/43d6d679-d80a-412b-a063-c42b6bb09734" />
