
<template>
    <v-container>
      <h1>Reusable Components</h1>
      <TextField :fields="text_sample" />
      <SelectField :fields="select_sample" />
      <RadioField :fields="radio_sample" />
      <TimeField :fields="time_sample" />
      {{time_sample.time}}
      <DateField :fields="date_sample" />
    </v-container>
</template>

<script>
import TextField from '~/components/inputs/TextField.vue';
import SelectField from '~/components/inputs/SelectField.vue';
import RadioField from '~/components/inputs/RadioField.vue';
import TimeField from '~/components/inputs/TimeField.vue';
import DateField from '~/components/inputs/DateField.vue';
export default {
  name: 'App',
  components: {
    TextField,
    SelectField,
    RadioField,
    TimeField,
    DateField
  },
  data: () => ({
    text_sample: {
      label: 'Enter Text',
      text: ''
    },
    select_sample: {
      label: 'Select Item',
      answers: ['Red', 'Blue', 'Green', 'Black'],
      selected: ''
    },
    radio_sample: {
      answers: ['Yes', 'No', 'Maybe'],
      selected: 'No'
    },
    date_sample: {
       label: 'Birthday',
       // you can define a default date e.g date = Date.now()
    },
    time_sample: {
      label: 'Curfew',
      // you can define a default time with correct format
    }
  }),
};
</script>
<style>

</style>