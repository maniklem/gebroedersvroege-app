<template>
  <div>
    <v-toolbar flat>
      <!-- Button toggle om te switchen tussen week en maand overzicht -->
      <v-btn-toggle v-model="type" tile group>
        <v-btn value="week">week</v-btn>
        <v-btn value="month">maand</v-btn>
      </v-btn-toggle>

      <!-- Navigatie naar maand/week terug en vooruit -->
      <v-btn icon @click="$refs.calendar.prev()">
        <v-icon>mdi-chevron-left</v-icon>
      </v-btn>
      <div v-if="type == 'week'">
        {{ formattedDateforWeekView }}
      </div>
      <div v-else-if="(type = 'month')">{{ formattedDateforMonthView }}</div>
      <v-btn icon @click="$refs.calendar.next()">
        <v-icon>mdi-chevron-right</v-icon>
      </v-btn>


    </v-toolbar>
    <v-toolbar flat>
      <!-- Button om event toe te voegen -->
      <event-dlg/>
    </v-toolbar>
    <v-sheet height="700" class="mt-2">
      <v-calendar
        ref="calendar"
        v-model="value"
        :weekdays="weekday"
        :type="type"
        :events="events"
        :event-overlap-mode="mode"
        :event-overlap-threshold="30"
        :event-color="getEventColor"
        :show-week="true"
        @change="getEvents"
      ></v-calendar>
    </v-sheet>
  </div>
</template>

<script>
import moment from "moment";
import EventDlg from "~/components/boerderij_kalender/EventDlg.vue";
export default {
  components: {
    EventDlg
  },
  data: () => ({
    type: "month",
    types: ["month", "week"],
    mode: "column",
    modes: ["stack", "column"],
    weekday: [0, 1, 2, 3, 4, 5, 6],
    weekdays: [
      { text: "Zon - Za", value: [0, 1, 2, 3, 4, 5, 6] },
      // { text: 'Mon - Sun', value: [1, 2, 3, 4, 5, 6, 0] },
      // { text: 'Mon - Fri', value: [1, 2, 3, 4, 5] },
      // { text: 'Mon, Wed, Fri', value: [1, 3, 5] },
    ],
    value: "",
    events: [],
    colors: [
      "blue",
      "indigo",
      "deep-purple",
      "cyan",
      "green",
      "orange",
      "grey darken-1",
    ],
    names: [
      "Meeting",
      "Holiday",
      "PTO",
      "Travel",
      "Event",
      "Birthday",
      "Conference",
      "Party",
    ],
  }),
  methods: {
    getEvents({ start, end }) {
      const events = [];

      const min = new Date(`${start.date}T00:00:00`);
      const max = new Date(`${end.date}T23:59:59`);
      const days = (max.getTime() - min.getTime()) / 86400000;
      const eventCount = this.rnd(days, days + 20);

      for (let i = 0; i < eventCount; i++) {
        const allDay = this.rnd(0, 3) === 0;
        const firstTimestamp = this.rnd(min.getTime(), max.getTime());
        const first = new Date(firstTimestamp - (firstTimestamp % 900000));
        const secondTimestamp = this.rnd(2, allDay ? 288 : 8) * 900000;
        const second = new Date(first.getTime() + secondTimestamp);
        console.log(first)
        console.log(second)

        events.push({
          name: this.names[this.rnd(0, this.names.length - 1)],
          start: first,
          end: second,
          color: this.colors[this.rnd(0, this.colors.length - 1)],
          timed: !allDay,
        });
      }

      this.events = events;
    },
    getEventColor(event) {
      return event.color;
    },
    rnd(a, b) {
      return Math.floor((b - a + 1) * Math.random()) + a;
    },
  },
  computed: {
    // Functies om datums te formatteren
    formattedDateforWeekView() {
      if (this.events.length > 0) {
        return moment(this.events[0].start).locale("nl").format("WW / YYYY");
      }
    },
    formattedDateforMonthView() {
      if (this.events.length > 0) {
        return moment(this.events[0].start).locale("nl").format("MMMM / YYYY");
      }
    },
  },
};
</script>
