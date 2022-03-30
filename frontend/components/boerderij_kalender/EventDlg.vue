<template>
  <v-dialog width="500">
    <template v-slot:activator="{ on, attrs }">
      <v-btn color="success" outlined v-bind="attrs" v-on="on">
        <v-icon left> mdi-plus-circle-outline </v-icon> Event toevoegen
      </v-btn>
    </template>
    <v-card>
      <v-card-title class="grey lighten-2">
        Event toevoegen
      </v-card-title>

      <v-card-text>
        <v-form class="mt-2">
          <!-- Van datum tijd -->
          <v-row>
            <v-col>
              <date-field :fields="from_date" />
              <time-field :fields="from_time" />
            </v-col>
            <v-col>
              <date-field :fields="to_date" />
              <time-field :fields="to_time" />
            </v-col>
          </v-row>

          <text-field :fields="event_title" />
          <text-area-field :fields="event_description" />
        </v-form>
      </v-card-text>

      <v-divider></v-divider>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="warning" outlined @click="dialog = false"> Annuleren </v-btn>
        <v-btn color="primary" outlined @click="dialog = false"> toevoegen </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import SelectField from "~/components/inputs/SelectField.vue";
import RadioField from "~/components/inputs/RadioField.vue";
import TimeField from "~/components/inputs/TimeField.vue";
import DateField from "~/components/inputs/DateField.vue";
import TextField from "../inputs/TextField.vue";
import TextAreaField from "../inputs/TextAreaField.vue";
export default {
  components: {
    SelectField,
    RadioField,
    TimeField,
    DateField,
    TextField,
    TextAreaField,
  },
  data: () => ({
    event_title: {
      label: "Titel",
      text: "",
    },
    event_description: {
      label: "Beschrijving",
      text: "",
    },
    from_date: {
      label: "Van datum",
      //    date : Date.now()
    },
    from_time: {
      label: "Van tijd",
      // you can define a default time with correct format
    },
    to_date: {
      label: "Tot datum",
      //    date : Date.now()
    },
    to_time: {
      label: "Tot tijd",
      // you can define a default time with correct format
    },
  }),
};
</script>

<style>
</style>