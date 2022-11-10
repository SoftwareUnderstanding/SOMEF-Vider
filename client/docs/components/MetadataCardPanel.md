# Metadata Card Panel

**Author:** Vitoriox

This is where the rest of the fields are displayed, grows or shrinks depending on the number of metadata
fields extracted. Depending on the type of object that is contained in the metadata field, the v-expansion-panel
will have a different configuration:
- If the content is an array, the expansion panel will contain a v-carousel component to show all the content of
  array
- If the content is not an array, the expansion panel will display the excerpt field as it is given by SOMEF.
  Except the *Citation* field, this field must be processed by the parseCitation() function before displaying it.

Inside the metadata card it will be used the following components: 
 - ConfidenceChip
 - ExtractMethodChip
 - Editor

```html
    <metadata-card-panel :id="id"
                         :threshold="threshold"
                         :title="title"
                         :content="content"
    />
```

## Props

| Name                   | Type     | Default | Description                                                                                                                             |
|------------------------|----------|---------|-----------------------------------------------------------------------------------------------------------------------------------------|
| `threshold` *required* | `Number` | 0       | Threshold value given by the user in the form. It's required to show properly the ConfidenceChip components.                            |
| `title` *required*     | `String` | ""      | Title to be displayed in the panel header                                                                                               |
| `id` *required*        | `String` | null    | Unique id for the panel, so it can be used later for navigation from the Tabs                                                           |
| `content` *required*   | `Array`  | null    | List of content objects, this objects must follow the next format:   {excerpt: (Any), confidence: (Number), extractionMethod: (String)} |


## Computed

### extractionMethodList()

This computed prop returns a Set of all the extraction methods used to obtain the metadata

**Syntax**

```typescript
extractionMethodList(): Set
```
