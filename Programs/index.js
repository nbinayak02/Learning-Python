import pkg from 'nepali-date-converter'
const NepaliDate = pkg.NepaliDate || pkg.default
const dates = [
  "2078-10-19",
  "2078-10-20",
  "2078-10-22",
  "2078-11-02",
  "2078-11-18",
  "2078-11-19",
  "2078-11-19",
  "2078-11-19",
  "2078-12-11",
  "2078-12-02",
  "2078-12-23",
  "2078-12-30",
  "2078-12-30",
  "2079-01-06",
  "2079-01-08",
  "2079-01-21",
  "2079-01-22",
  "2079-01-23",
  "2079-02-24",
  "2078-03-26",
  "2078-03-27"
];

const timestamps = dates.map((d) => {
 const dt = new NepaliDate(d).toJsDate();
 return dt;
});

timestamps.forEach(t => {
  console.log(t);
})
