# SOMEF Form

**Author:** Vitoriox

Formulary where user input is collected for calling SOMEF.

```html
<somef-form @submit="submitForm"/>
```
## Data

| Name                | Type      | Initial value | Description                                               |
|---------------------|-----------|---------------|-----------------------------------------------------------|
| `url`               | `String`  | `Null`        | Value of the GitHub URL field in the form                 |
| `threshold`         | `Number`  | `Null`        | Value of the threshold given in the form                  |
| `ignoreClassifiers` | `Boolean` | `False`       | Flag for ignoring classifiers. By default is always false |
| `rules`             | `Object`  |               | Rules used for validating each of the form fields         |

## Events

| Name     | Payload                                 | Description                                                       |
|----------|-----------------------------------------|-------------------------------------------------------------------|
| `submit` | `url`, `threshold`, `ignoreClassifiers` | Emitted when the clicked "SUBMIT" button and the fields are valid |

## Methods

### submit()

Called when user clicks at "SUBMIT" button. Validates al form fields and emits the `submit` event

**Syntax**

```typescript
submit(): void
```
