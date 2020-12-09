resource "aws_route53_zone" "my_zone" {
  name = "abcd.xyz"
}

resource "aws_route53_record" "server1-record" {
  zone_id = aws_route53_zone.my_zone.zone_id
  name    = "web.abcd.xyz"
  type    = "A"
  alias {
    name                   = aws_elb.my-elb.dns_name
    zone_id                = aws_elb.my-elb.zone_id
    evaluate_target_health = true
  }
}

output "ns-servers" {
  value = aws_route53_zone.newtech-academy.name_servers
}

